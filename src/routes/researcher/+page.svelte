<script>
  import { onMount } from 'svelte';
  import { fade, fly } from 'svelte/transition';
  import { goto } from '$app/navigation';
  import { auth } from '$lib/auth';
  import ChatBox from '$lib/components/ChatBox.svelte';
  import FileUpload from '$lib/components/FileUpload.svelte';
  import { Search, FileText, BarChart, Book } from 'lucide-svelte';

  let user;

  onMount(() => {
    const unsubscribe = auth.subscribe(value => {
      user = value;
      if (!value.isAuthenticated || value.userType !== 'researcher') {
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
  <title>Researcher Dashboard - HealthCare Plus</title>
</svelte:head>

<div class="min-h-screen bg-gray-100">
  <nav class="bg-white shadow-lg">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <div class="flex-shrink-0 flex items-center">
            <img class="h-8 w-auto" src="src/lib/assets/icons/research.svg" alt="HealthCare Plus">
          </div>
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            <a href="#" class="border-indigo-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
              Dashboard
            </a>
          </div>
        </div>
        <div class="hidden sm:ml-6 sm:flex sm:items-center">
          <button
            on:click={handleLogout}
            class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  </nav>

  <header class="bg-white shadow">
    <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-gray-900">Welcome, Researcher {user?.user || ''}</h1>
    </div>
  </header>

  <main>
    <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <div class="grid md:grid-cols-2 gap-8">
          <div in:fly={{ x: -50, duration: 500, delay: 300 }} out:fade>
            <div class="bg-white overflow-hidden shadow rounded-lg divide-y divide-gray-200">
              <div class="px-4 py-5 sm:px-6">
                <h2 class="text-lg font-medium text-gray-900">Research Tools</h2>
              </div>
              <div class="px-4 py-5 sm:p-6">
                <div class="grid grid-cols-2 gap-4">
                  <button class="bg-indigo-50 p-4 rounded-lg flex flex-col items-center justify-center transition duration-300 hover:bg-indigo-100">
                    <Search class="h-8 w-8 text-indigo-600" />
                    <span class="mt-2 text-sm font-medium text-gray-900">Literature Search</span>
                  </button>
                  <button class="bg-indigo-50 p-4 rounded-lg flex flex-col items-center justify-center transition duration-300 hover:bg-indigo-100">
                    <FileText class="h-8 w-8 text-indigo-600" />
                    <span class="mt-2 text-sm font-medium text-gray-900">Research Proposals</span>
                  </button>
                  <button class="bg-indigo-50 p-4 rounded-lg flex flex-col items-center justify-center transition duration-300 hover:bg-indigo-100">
                    <BarChart class="h-8 w-8 text-indigo-600" />
                    <span class="mt-2 text-sm font-medium text-gray-900">Data Analysis</span>
                  </button>
                  <button class="bg-indigo-50 p-4 rounded-lg flex flex-col items-center justify-center transition duration-300 hover:bg-indigo-100">
                    <Book class="h-8 w-8 text-indigo-600" />
                    <span class="mt-2 text-sm font-medium text-gray-900">Publications</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div in:fly={{ x: 50, duration: 500, delay: 300 }} out:fade>
            <div class="bg-white overflow-hidden shadow rounded-lg">
              <div class="px-4 py-5 sm:p-6">
                <h2 class="text-lg font-medium text-gray-900 mb-4">Research Inquiry Chat</h2>
                <ChatBox userType="researcher" />
              </div>
            </div>
          </div>
        </div>
        <div class="mt-8" in:fly={{ y: 50, duration: 500, delay: 600 }} out:fade>
          <div class="bg-white overflow-hidden shadow rounded-lg">
            <div class="px-4 py-5 sm:p-6">
              <h2 class="text-lg font-medium text-gray-900 mb-4">Upload Research Documents</h2>
              <FileUpload />
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</div>