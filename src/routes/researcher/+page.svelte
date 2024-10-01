<script>
    import { fade, fly } from 'svelte/transition';
    import ChatBox from '$lib/components/ChatBox.svelte';
    import FileUpload from '$lib/components/FileUpload.svelte';
  </script>
  
  <svelte:head>
    <title>Researcher Dashboard - HealthCare Plus</title>
  </svelte:head>
  
  <div class="min-h-screen bg-gray-100">
    <header class="bg-white shadow" in:fade={{ duration: 300, delay: 300 }}>
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-900">Researcher Dashboard</h1>
      </div>
    </header>
    <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div class="px-4 py-6 sm:px-0">
          <div class="grid md:grid-cols-2 gap-8">
            <div in:fly={{ x: -50, duration: 500, delay: 300 }} out:fade>
              <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="px-4 py-5 sm:p-6">
                  <h2 class="text-2xl font-semibold mb-4">Upload Research Documents</h2>
                  <FileUpload />
                </div>
              </div>
            </div>
            <div in:fly={{ x: 50, duration: 500, delay: 300 }} out:fade>
              <div class="bg-white overflow-hidden shadow rounded-lg">
                <div class="px-4 py-5 sm:p-6">
                  <h2 class="text-2xl font-semibold mb-4">Research Inquiry Chat</h2>
                  <ChatBox userType="researcher" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>