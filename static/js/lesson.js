let pyodide = null;
const statusEl = document.getElementById("runtimeStatus");
const outputEl = document.getElementById("codeOutput");
const editor = document.getElementById("codeInput");
const runBtn = document.getElementById("runCode");
const resetBtn = document.getElementById("resetCode");

async function loadPython(){
  try{
    if(typeof loadPyodide === "undefined") throw new Error("Pyodide library did not load. Check your internet connection and refresh.");
    pyodide = await loadPyodide();
    statusEl.textContent = "Python ready";
    statusEl.classList.remove("loading");
  }catch(err){
    statusEl.textContent = "Python unavailable";
    statusEl.classList.add("loading");
    outputEl.textContent = err.message;
  }
}
loadPython();

runBtn.addEventListener("click", async()=>{
  if(!pyodide){outputEl.textContent="Python is still loading, or could not load. Refresh and check your internet connection.";return;}
  outputEl.textContent="Running…";
  try{
    let printed = [];
    pyodide.setStdout({batched:(s)=>printed.push(s)});
    pyodide.setStderr({batched:(s)=>printed.push(s)});
    await pyodide.runPythonAsync(editor.value);
    outputEl.textContent = printed.join("") || "(Program finished with no printed output.)";
  }catch(err){outputEl.textContent=String(err);}
});
resetBtn.addEventListener("click",()=>{editor.value='# Write your Python code here\nprint("Hello, Codoria!")';outputEl.textContent="Editor reset.";});
function copyExample(){copyText(exampleCode);}
window.copyExample = copyExample;

document.querySelectorAll(".quiz-option").forEach(btn=>{
  btn.addEventListener("click",()=>{
    document.querySelectorAll(".quiz-option").forEach(b=>b.classList.remove("selected","correct","wrong"));
    const picked = Number(btn.dataset.index);
    btn.classList.add("selected");
    const feedback = document.getElementById("quizFeedback");
    const explanation = document.getElementById("quizExplanation");
    if(picked===correctAnswer){
      btn.classList.add("correct");
      if(window.playSound) window.playSound("win");
      feedback.textContent="Correct! The kingdom's knowledge grows. ✦";
      explanation.style.display="block";
      document.getElementById("completeMission").disabled=false;
    }else{
      btn.classList.add("wrong");
      if(window.playSound) window.playSound("error");
      feedback.textContent="Not quite. Try again, explorer!";
      explanation.style.display="none";
      document.getElementById("completeMission").disabled=true;
    }
  });
});

document.getElementById("completeMission").addEventListener("click",async()=>{
  const button=document.getElementById("completeMission");
  button.disabled=true;
  try{
    const response=await fetch(`/complete/${worldId}`,{method:"POST"});
    const result=await response.json();
    if(!result.ok) throw new Error(result.message || "Could not save progress.");
    if(window.playSound) window.playSound("unlock");
    document.getElementById("completeMessage").textContent=`Mission complete! You earned 100 XP. Total XP: ${result.xp}. Returning to your map…`;
    button.textContent="Mission completed ✓";
    setTimeout(()=>window.location.href="/adventure",1600);
  }catch(err){
    document.getElementById("completeMessage").textContent=err.message;
    button.disabled=false;
  }
});
