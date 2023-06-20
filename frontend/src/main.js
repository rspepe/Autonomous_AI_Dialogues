// main.js
import './main.css';
import { createApp } from "vue";
import App from "./App.vue";
import axios from "axios";
import { createMetaManager } from "vue-meta";

const app = createApp(App);

app.config.globalProperties.$http = axios;

// ここで vue-meta を使用します
const metaManager = createMetaManager({
  refreshOnceOnNavigation: true,
});
app.use(metaManager);

app.mount("#app");
