(()=>{
  const mount=document.getElementById('tss-header-de');
  if(!mount)return;

  const base='/wp-content/uploads/tshirtswiss-elementor-kit/assets/header/de/';
  const fragments=['topbar.html','desktop-header.html','mobile-panel.html'];

  const fetchText=async file=>{
    const response=await fetch(base+file,{credentials:'same-origin'});
    if(!response.ok)throw new Error(`Failed to load ${file}: ${response.status}`);
    return response.text();
  };

  Promise.all(fragments.map(fetchText))
    .then(parts=>{
      mount.outerHTML=parts.join('');
      const script=document.createElement('script');
      script.src=base+'mobile.js';
      script.defer=true;
      document.body.appendChild(script);
    })
    .catch(error=>{
      console.error('TShirtSwiss German header failed to load.',error);
    });
})();
