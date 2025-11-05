## _includes/head/
```html
<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
```

## _includes/footer.html
```html
<script>
  // Show the button when user scrolls down 100px
  window.onscroll = function() {
    const btn = document.getElementById("back-to-top");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
      btn.style.display = "block";
    } else {
      btn.style.display = "none";
    }
  };

  // Smooth scroll to top
  document.getElementById("back-to-top").addEventListener("click", function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
</script>
```

## _sass/minima/custom.scss

## _config.yml
- theme: null
