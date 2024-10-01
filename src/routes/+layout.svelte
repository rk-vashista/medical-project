<script>
    import '../app.css';
    import { fade } from 'svelte/transition';
    import Header from '$lib/components/Header.svelte';
    import Footer from '$lib/components/Footer.svelte';
  </script>
  
  <div class="flex flex-col min-h-screen">
    <Header />
    <main class="flex-grow" in:fade={{ duration: 300, delay: 300 }} out:fade={{ duration: 300 }}>
      <slot />
    </main>
    <Footer />
  </div>