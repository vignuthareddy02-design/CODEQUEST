const form=document.getElementById('assessmentForm');
const resultBox=document.getElementById('assessmentResult');
const submitButton=document.getElementById('submitAssessment');
const timerNode=document.getElementById('assessmentTimer');
let seconds=ASSESSMENT_DURATION*60;
let submitted=false;
function updateProgress(){
  const answered=document.querySelectorAll('.assessment-question input:checked').length;
  document.getElementById('answeredCount').textContent=answered;
  document.getElementById('assessmentProgressBar').style.width=(answered/ASSESSMENT_COUNT*100)+'%';
}
document.querySelectorAll('.assessment-question input').forEach(input=>input.addEventListener('change',updateProgress));
const timer=setInterval(()=>{
  if(submitted){clearInterval(timer);return;}
  seconds--;
  timerNode.textContent=String(Math.floor(seconds/60)).padStart(2,'0')+':'+String(seconds%60).padStart(2,'0');
  if(seconds<=0){clearInterval(timer);form.requestSubmit();}
},1000);
form.addEventListener('submit',async event=>{
  event.preventDefault();if(submitted)return;
  submitted=true;clearInterval(timer);submitButton.disabled=true;submitButton.textContent='Evaluating…';
  const answers={};
  document.querySelectorAll('.assessment-question').forEach(card=>{
    const selected=card.querySelector('input:checked');if(selected)answers[card.dataset.qid]=Number(selected.value);
  });
  try{
    const response=await fetch(`/python/submit/${ASSESSMENT_KIND}/${ASSESSMENT_MODULE}`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(answers)});
    const result=await response.json();if(!result.ok)throw new Error(result.message || 'Assessment could not be saved.');
    form.hidden=true;
    resultBox.hidden=false;
    resultBox.innerHTML=`<div class="result-score">${result.score}%</div><h2>${result.passed?'Trial passed! ✨':'Keep practising, explorer.'}</h2><p>${result.correct} correct out of ${result.total}. ${result.passed?'You met the 70% pass mark.':'You need at least 70% to pass. Review the explanations and retry.'}</p><div class="result-analysis"></div><a class="btn btn-gold" href="${result.next_url}">${result.passed?(ASSESSMENT_KIND==='exam'?'Continue your adventure':'Return to module'):'Review and retry'} →</a>`;
    const analysis=resultBox.querySelector('.result-analysis');
    const categorySummary=document.createElement('div');categorySummary.className='category-summary';
    Object.entries(result.type_summary || {}).forEach(([type,stats])=>{const row=document.createElement('p');row.textContent=`${type.replaceAll('_',' ')}: ${stats.correct}/${stats.total} correct (${stats.score}%)`;categorySummary.append(row);});
    analysis.append(categorySummary);
    result.analysis.forEach((item,index)=>{
      const block=document.createElement('article');block.className='analysis-item '+(item.is_correct?'analysis-correct':'analysis-wrong');
      const heading=document.createElement('b');heading.textContent=`${index+1}. ${item.is_correct?'Correct':'Review this answer'}`;
      const question=document.createElement('p');question.textContent=item.question;
      const correct=document.createElement('p');correct.textContent='Correct answer: '+item.options[item.correct_answer];
      const explanation=document.createElement('p');explanation.textContent=item.explanation;
      block.append(heading,question,correct,explanation);analysis.append(block);
    });
  }catch(error){submitted=false;submitButton.disabled=false;submitButton.textContent='Try submit again';resultBox.hidden=false;resultBox.textContent=error.message;}
});
