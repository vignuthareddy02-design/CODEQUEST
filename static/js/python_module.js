let pyRuntime = null;
const statusNode = document.getElementById('runtimeStatus');
const outputNode = document.getElementById('codeOutput');
const editorNode = document.getElementById('codeInput');
async function initPythonRuntime(){
  try{
    if(typeof loadPyodide === 'undefined') throw new Error('Python runner did not load. Check your internet connection and refresh.');
    pyRuntime = await loadPyodide();
    statusNode.textContent = 'Python ready';
  }catch(error){ statusNode.textContent = 'Runner unavailable'; outputNode.textContent = error.message; }
}
initPythonRuntime();
document.getElementById('runCode').addEventListener('click', async()=>{
  if(!pyRuntime){outputNode.textContent='Python is still loading or could not load. Refresh and check your internet connection.';return;}
  outputNode.textContent='Running…';
  try{
    const printed=[];
    pyRuntime.setStdout({batched:s=>printed.push(s)});
    pyRuntime.setStderr({batched:s=>printed.push(s)});
    await pyRuntime.runPythonAsync(editorNode.value);
    outputNode.textContent=printed.join('') || '(Program finished with no printed output.)';
  }catch(error){outputNode.textContent=String(error);}
});
document.getElementById('resetCode').addEventListener('click',()=>{editorNode.value='# Try a small example\nprint("Hello, Python Kingdom!")';outputNode.textContent='Editor reset.';});
window.copyPythonExample = async code => { try { await navigator.clipboard.writeText(code); if(window.playSound) window.playSound('win'); } catch(e) { outputNode.textContent='Clipboard access was blocked. Select and copy the code manually.'; } };
window.togglePracticeInfo = (button, kind) => {
  const card=button.closest('.practice-card');
  const target=card.querySelector(kind==='hint'?'.practice-hint':'.practice-solution');
  target.hidden=!target.hidden;
  button.textContent=(target.hidden?'Show ':'Hide ')+(kind==='hint'?'hint':'solution approach');
};
window.savePractice = async button => {
  const card=button.closest('.practice-card');
  const answer=card.querySelector('.practice-answer').value;
  const status=card.querySelector('.practice-saved');
  if(!answer.trim()){status.textContent='Write an attempt before saving.';return;}
  const response=await fetch(`/python/practice/${PY_MODULE_ID}/${card.dataset.practice}`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({answer})});
  const result=await response.json();status.textContent=result.message || 'Could not save your attempt.';
};
document.getElementById('markLesson').addEventListener('click',async()=>{
  const button=document.getElementById('markLesson');button.disabled=true;
  try{const response=await fetch(`/python/complete-lesson/${PY_MODULE_ID}`,{method:'POST'});const result=await response.json();if(!result.ok)throw new Error(result.message);button.textContent='Lesson complete ✓';button.insertAdjacentHTML('afterend','<p class="sidebar-note">Lesson saved. Take the topic quiz to unlock your examination.</p>');}
  catch(error){button.disabled=false;button.textContent='Try again';alert(error.message);}
});
