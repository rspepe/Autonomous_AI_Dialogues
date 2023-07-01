<!-- src/App.vue -->
<template>
  <div class="chat-container" ref="chatContainer">
    <ChatBubble
      v-for="(message, index) in visibleMessages"
      :key="index"
      :name="message.name"
      :text="message.message"
      :visible_from="message.visible_from"
    />
  </div>
</template>

<script>
import ChatBubble from './components/ChatBubble.vue'
import { useMeta } from 'vue-meta'

export default {
  setup() {
    useMeta({
      title: 'Autonomous AI Dialogues',
    })
  },
  name: 'App',
  components: {
    ChatBubble,
  },
  data() {
    return {
      conversation: { results: [] },
      now: new Date().toISOString(), // 現在の時刻を管理するデータプロパティ
    }
  },
  computed: {
    visibleMessages() {
      return this.conversation.results.filter(
        message => message.visible_from <= this.now // 現在の時刻を使って計算
      )
    },
  },
  created() {
    this.fetchConversation()
    setInterval(this.fetchConversation, 30 * 60 * 1000) // 30分ごとにfetchConversationを呼び出す
    setInterval(() => {
      this.now = new Date().toISOString()
    }, 1000) // 1秒ごとに現在の時刻を更新
  },
  methods: {
    async fetchConversation() {
      try {
        const response = await this.$http.get('conversation_history.json')
        this.conversation = response.data
        this.$nextTick(() => {
          window.scrollTo(0, document.body.scrollHeight)
        })
      } catch (error) {
        // console.error('Error fetching conversation:', error)
      }
    },
  },
}
</script>

<style>
#app {
  padding-left: 10px;
  padding-right: 10px;
}
</style>
