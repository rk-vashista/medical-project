<script>
    import { page } from '$app/stores';
  </script>
  
  <header class="bg-white shadow">
    <nav class="container mx-auto px-4 py-4 flex justify-between items-center">
      <a href="/" class="text-2xl font-bold text-indigo-600">HealthCare Plus</a>
      <div>
        {#if $page.url.pathname !== '/login'}
          <a href="/login" class="text-gray-600 hover:text-gray-900">Login</a>
        {:else}
          <a href="/" class="text-gray-600 hover:text-gray-900">Home</a>
        {/if}
      </div>
    </nav>
  </header>