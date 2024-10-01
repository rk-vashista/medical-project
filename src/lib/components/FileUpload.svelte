<script>
  import { fade } from 'svelte/transition';
  import { uploadFile } from '$lib/utils/api';

  let file;
  let uploadStatus = '';

  async function handleSubmit() {
    if (file) {
      uploadStatus = 'Uploading...';
      try {
        await uploadFile(file);
        uploadStatus = 'File uploaded successfully!';
      } catch (error) {
        uploadStatus = 'Error uploading file. Please try again.';
      }
    }
  }
</script>

<div class="bg-white shadow rounded-lg p-4">
  <form on:submit|preventDefault={handleSubmit}>
    <div class="mb-4">
      <label for="file" class="block text-gray-700 font-bold mb-2">Choose a file:</label>
      <input
        type="file"
        id="file"
        accept=".pdf,.doc,.docx"
        bind:files={file}
        class="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>
    <button
      type="submit"
      class="w-full px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500"
    >
      Upload
    </button>
  </form>
  {#if uploadStatus}
    <p class="mt-4 text-center" in:fade={{ duration: 300 }}>
      {uploadStatus}
    </p>
  {/if}
</div>