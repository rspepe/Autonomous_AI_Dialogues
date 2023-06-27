<!-- src/components/ChatBubble.vue -->
<template>
  <div class="chat-bubble" :class="name">
    <h3>{{ name }}</h3>
    <p class="message">{{ text }}</p>
    <p class="datetime">{{ formattedTime }}</p>
  </div>
</template>

<script>
export default {
  name: 'ChatBubble',
  props: {
    name: String,
    text: String,
    visible_from: String,
  },
  computed: {
    formattedTime() {
      if (!this.visible_from) return ''
      let date = new Date(this.visible_from)
      date.setHours(date.getHours() + 9)
      return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    },
  },
}
</script>

<style scoped>
.chat-bubble {
  display: flex;
  align-items: flex-start;
  color: #333;
  margin-bottom: 5px;
}

.chat-bubble h3 {
  text-align: center;
  line-height: 2.5;
  width: 50px;
  height: 50px;
  border-radius: 25px;
  background-color: white;
}

.chat-bubble p.message {
  margin: auto 10px;
  padding: 10px;
  border-radius: 10px;
  flex: 1;
}

.AI1 {
  flex-direction: row;
}

.AI1 p.message {
  background: white;
}

.AI2 {
  flex-direction: row-reverse;
}
.AI2 p.message {
  background: #94df83;
}

p.datetime {
  margin-top: auto;
}
</style>
