<script>
  import { fade, fly } from 'svelte/transition';
  import { sendMessage } from '$lib/utils/api';

  export let userType;

  let messages = [];
  let newMessage = '';

  async function handleSubmit() {
    if (newMessage.trim()) {
      messages = [...messages, { text: newMessage, sender: 'You' }];
      const response = await sendMessage(newMessage, userType);
      messages = [...messages, { text: response, sender: 'Support' }];
      newMessage = '';
    }
  }
</script>

<div class="bg-white shadow rounded-lg p-4">
  <div class="h-64 overflow-y-auto mb-4">
    {#each messages as message (message.text)}
      <div
        class="mb-2"
        class:text-right={message.sender === 'You'}
        in:fly={{ y: 20, duration: 300 }}
        out:fade={{ duration: 300 }}
      >
        <span
          class="inline-block px-2 py-1 rounded"
          class:bg-blue-500={message.sender === 'You'}
          class:text-white={message.sender === 'You'}
          class:bg-gray-200={message.sender !== 'You'}
        >
          {message.text}
        </span>
      </div>
    {/each}
  </div>
  <form on:submit|preventDefault={handleSubmit} class="flex">
    <input
      type="text"
      bind:value={newMessage}
      placeholder="Type your message..."
      class="flex-grow mr-2 px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors duration-300"
    />
    <button
      type="submit"
      class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors duration-300"
    >
      Send
    </button>
  </form>
</div>