(()=>{
  const panel=document.querySelector('.tss-mobile-panel');
  const overlay=document.querySelector('.tss-mobile-overlay');
  const toggle=document.querySelector('.tss-mobile-toggle');
  const close=document.querySelector('.tss-mobile-panel__close');
  if(!panel||!overlay||!toggle)return;

  const setOpen=open=>{
    panel.classList.toggle('is-open',open);
    overlay.hidden=!open;
    panel.setAttribute('aria-hidden',String(!open));
    toggle.setAttribute('aria-expanded',String(open));
    document.body.classList.toggle('tss-mobile-menu-open',open);
  };

  toggle.addEventListener('click',()=>setOpen(true));
  if(close)close.addEventListener('click',()=>setOpen(false));
  overlay.addEventListener('click',()=>setOpen(false));
  document.addEventListener('keydown',event=>{
    if(event.key==='Escape')setOpen(false);
  });
})();
