(()=>{
  const mount=document.getElementById('tss-footer-de');
  if(!mount)return;

  const url='/wp-content/uploads/tshirtswiss-elementor-kit/assets/footer/de/footer.html';
  fetch(url,{credentials:'same-origin'})
    .then(response=>{
      if(!response.ok)throw new Error(`Failed to load footer: ${response.status}`);
      return response.text();
    })
    .then(html=>{mount.outerHTML=html;})
    .catch(error=>{console.error('TShirtSwiss German footer failed to load.',error);});
})();
