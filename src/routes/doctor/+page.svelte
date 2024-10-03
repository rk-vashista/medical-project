<script lang="ts">
  import { onMount } from 'svelte';
  import { fade, fly } from 'svelte/transition';
  import { goto } from '$app/navigation';
  import { auth } from '$lib/auth';
  import ChatBox from '$lib/components/ChatBox.svelte';
  import FileUpload from '$lib/components/FileUpload.svelte';

  let user;

  onMount(() => {
    const unsubscribe = auth.subscribe(value => {
      user = value;
      if (!value.isAuthenticated || value.userType !== 'doctor') {
        goto('/');
      }
    });

    return unsubscribe;
  });

  function handleLogout() {
    auth.logout();
    goto('/');
  }
</script>

<svelte:head>
  <title>Doctor Dashboard - HealthCare Plus</title>
</svelte:head>

<div class="min-h-screen bg-gray-100">
  <header class="bg-white shadow" in:fade={{ duration: 300, delay: 300 }}>
    <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
      <h1 class="text-3xl font-bold text-gray-900">Doctor Dashboard</h1>
      <button
        on:click={handleLogout}
        class="px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-colors duration-300"
      >
        Logout
      </button>
    </div>
  </header>
  <main>
    <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <div class="grid md:grid-cols-2 gap-8">
          <div in:fly={{ x: -50, duration: 500, delay: 300 }} out:fade>
            <div class="bg-white overflow-hidden shadow rounded-lg">
              <div class="px-4 py-5 sm:p-6">
                <h2 class="text-2xl font-semibold mb-4">Upload Patient Records</h2>
                <FileUpload />
              </div>
            </div>
          </div>
          <div in:fly={{ x: 50, duration: 500, delay: 300 }} out:fade>
            <div class="bg-white overflow-hidden shadow rounded-lg">
              <div class="px-4 py-5 sm:p-6">
                <h2 class="text-2xl font-semibold mb-4">Medical Consultation Chat</h2>
                <ChatBox userType="doctor" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</div>