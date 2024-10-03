import { writable } from 'svelte/store';

const createAuth = () => {
  const { subscribe, set, update } = writable({
    isAuthenticated: false,
    user: null,
    userType: null,
  });

  return {
    subscribe,
    login: async (username, password, userType) => {
      // In a real application, you would make an API call here
      await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate API call
      
      if (username === 'demo' && password === 'password') {
        set({ isAuthenticated: true, user: username, userType });
      } else {
        throw new Error('Invalid credentials');
      }
    },
    register: async (username, password, userType) => {
      // In a real application, you would make an API call here
      await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate API call
      
      set({ isAuthenticated: true, user: username, userType });
    },
    logout: () => {
      set({ isAuthenticated: false, user: null, userType: null });
    },
  };
};

export const auth = createAuth();