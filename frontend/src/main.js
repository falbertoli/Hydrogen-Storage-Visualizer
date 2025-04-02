// frontend/src/main.js
import { createApp } from "vue";
import { createStore } from "vuex";
import App from "./App.vue";
import "./style.css";

// Create Vuex store
const store = createStore({
  state() {
    return {
      facilities: [],
      regulations: [],
      storageConfig: null,
    };
  },
  mutations: {
    setFacilities(state, facilities) {
      state.facilities = facilities;
    },
    setRegulations(state, regulations) {
      state.regulations = regulations;
    },
    setStorageConfig(state, config) {
      state.storageConfig = config;
    },
  },
  actions: {
    async fetchFacilities({ commit }) {
      // Will implement API call later
    },
    async fetchRegulations({ commit }) {
      // Will implement API call later
    },
  },
});

const app = createApp(App);
app.use(store);
app.mount("#app");
