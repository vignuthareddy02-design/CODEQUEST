// CODEQUEST game feel: tiny synthesized UI sounds (no external audio files required).
let audioContext = null;
let soundEnabled = localStorage.getItem('cq-sound') !== 'off';
let musicEnabled = localStorage.getItem('cq-music') === 'on';
let musicTimer = null;
function getAudio(){
  const Ctx = window.AudioContext || window.webkitAudioContext;
  if(!Ctx) return null;
  if(!audioContext) audioContext = new Ctx();
  if(audioContext.state === 'suspended') audioContext.resume();
  return audioContext;
}
function tone(freq, duration=.12, type='sine', volume=.035, delay=0){
  const ctx=getAudio(); if(!ctx) return;
  const osc=ctx.createOscillator(), gain=ctx.createGain();
  osc.type=type; osc.frequency.setValueAtTime(freq,ctx.currentTime+delay);
  gain.gain.setValueAtTime(.0001,ctx.currentTime+delay);
  gain.gain.exponentialRampToValueAtTime(volume,ctx.currentTime+delay+.015);
  gain.gain.exponentialRampToValueAtTime(.0001,ctx.currentTime+delay+duration);
  osc.connect(gain);gain.connect(ctx.destination);osc.start(ctx.currentTime+delay);osc.stop(ctx.currentTime+delay+duration+.03);
}
function playSound(kind='click'){
  if(!soundEnabled) return;
  if(kind==='win'){[523,659,784,1047].forEach((f,i)=>tone(f,.22,'triangle',.045,i*.09));}
  else if(kind==='unlock'){[440,554,659,880].forEach((f,i)=>tone(f,.17,'sine',.035,i*.075));}
  else if(kind==='error'){tone(190,.2,'sawtooth',.025);}
  else {tone(660,.07,'sine',.018);}
}
function startMusic(){
  stopMusic(); if(!musicEnabled) return;
  const notes=[261.63,329.63,392,329.63,293.66,349.23,440,349.23];let i=0;
  musicTimer=setInterval(()=>{if(musicEnabled){tone(notes[i%notes.length],.48,'sine',.008);tone(notes[(i+2)%notes.length]*2,.35,'triangle',.003,.03);i++;}},620);
}
function stopMusic(){if(musicTimer){clearInterval(musicTimer);musicTimer=null;}}
function syncSoundButtons(){
  const s=document.getElementById('soundToggle'),m=document.getElementById('musicToggle');
  if(s){s.textContent=soundEnabled?'🔊':'🔇';s.classList.toggle('is-muted',!soundEnabled);}
  if(m){m.textContent=musicEnabled?'♫':'♪';m.classList.toggle('is-muted',!musicEnabled);}
}
document.addEventListener('DOMContentLoaded',()=>{
  syncSoundButtons(); if(musicEnabled) startMusic();
  document.getElementById('soundToggle')?.addEventListener('click',()=>{soundEnabled=!soundEnabled;localStorage.setItem('cq-sound',soundEnabled?'on':'off');syncSoundButtons();if(soundEnabled)playSound();});
  document.getElementById('musicToggle')?.addEventListener('click',()=>{musicEnabled=!musicEnabled;localStorage.setItem('cq-music',musicEnabled?'on':'off');syncSoundButtons();if(musicEnabled)startMusic();else stopMusic();playSound();});
  document.querySelectorAll('a,button').forEach(el=>{if(!el.id?.includes('Toggle'))el.addEventListener('click',()=>playSound('click'));});
  document.querySelectorAll('.level-open .level-orb').forEach(el=>el.addEventListener('click',()=>playSound('unlock')));
  document.querySelectorAll('.language-card:not(.disabled-course)').forEach(el=>el.addEventListener('mouseenter',()=>playSound('click'),{once:true}));
});
function copyText(text){if(navigator.clipboard){navigator.clipboard.writeText(text).then(()=>{playSound('win');alert('Copied to clipboard!');});}else{alert('Clipboard is unavailable in this browser.');}}
