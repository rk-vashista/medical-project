<script>
  import { fade, fly } from 'svelte/transition';
  import { goto } from '$app/navigation';
  import { auth } from '$lib/auth';

  let isLogin = true;
  let userType = 'patient';
  let username = '';
  let password = '';
  let error = '';

  const toggleForm = () => {
    isLogin = !isLogin;
    error = '';
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    error = '';

    try {
      if (isLogin) {
        await auth.login(username, password, userType);
      } else {
        await auth.register(username, password, userType);
      }
      goto(`/${userType}`);
    } catch (err) {
      error = err.message;
    }
  };

  const userTypes = [
    { value: 'patient', label: 'Patient' },
    { value: 'doctor', label: 'Doctor' },
    { value: 'researcher', label: 'Researcher' },
    { value: 'intern', label: 'Intern/Student' }
  ];
</script>

<svelte:head>
  <title>{isLogin ? 'Login' : 'Sign Up'} - HealthCare Plus</title>
</svelte:head>

<div class="min-h-screen flex items-center justify-center bg-cover bg-center transition-all duration-500 ease-in-out" style="background-image: url('https://images.unsplash.com/photo-1505751172876-fa1923c5c528?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');">
  <div class="max-w-md w-full space-y-8 bg-white bg-opacity-90 p-10 rounded-xl shadow-2xl" in:fade={{ duration: 300 }} out:fade={{ duration: 300 }}>
    <div>
      <h2 class="mt-6 text-center text-4xl font-extrabold text-gray-900">
        {isLogin ? 'Sign in to your account' : 'Create a new account'}
      </h2>
      <p class="mt-2 text-center text-sm text-gray-600">
        {isLogin ? "Don't have an account?" : "Already have an account?"}
        <button on:click={toggleForm} class="font-medium text-indigo-600 hover:text-indigo-500 transition-colors duration-300">
          {isLogin ? "Sign up" : "Sign in"}
        </button>
      </p>
    </div>
    <form class="mt-8 space-y-6" on:submit={handleSubmit}>
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="user-type" class="sr-only">User Type</label>
          <select
            id="user-type"
            bind:value={userType}
            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm transition-colors duration-300"
          >
            {#each userTypes as { value, label }}
              <option {value}>{label}</option>
            {/each}
          </select>
        </div>
        <div>
          <label for="username" class="sr-only">Username</label>
          <input
            id="username"
            name="username"
            type="text"
            required
            bind:value={username}
            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm transition-colors duration-300"
            placeholder="Username"
          />
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input
            id="password"
            name="password"
            type="password"
            required
            bind:value={password}
            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm transition-colors duration-300"
            placeholder="Password"
          />
        </div>
      </div>

      {#if error}
        <p class="text-red-500 text-sm text-center">{error}</p>
      {/if}

      <div>
        <button
          type="submit"
          class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-300"
        >
          <span class="absolute left-0 inset-y-0 flex items-center pl-3">
            <svg class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400 transition-colors duration-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
            </svg>
          </span>
          {isLogin ? 'Sign in' : 'Sign up'}
        </button>
      </div>
    </form>
  </div>
</div>