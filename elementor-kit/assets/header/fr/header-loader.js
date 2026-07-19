(()=>{
  const mount=document.getElementById('tss-header-fr');
  if(!mount)return;

  const base='/wp-content/uploads/tshirtswiss-elementor-kit/assets/header/fr/';
  const fragments=[
    'desktop-header-part-1.html',
    'desktop-header-part-2.html',
    'desktop-header-part-3.html',
    'desktop-header-part-4a.html',
    'desktop-header-part-4b.html',
    'desktop-header-part-5a.html',
    'desktop-header-part-5b.html',
    'desktop-header-part-5c.html',
    'mobile-panel.html'
  ];

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
      console.error('TShirtSwiss French header failed to load.',error);
    });
})();
