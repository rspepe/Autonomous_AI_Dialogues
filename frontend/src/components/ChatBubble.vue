<!-- src/components/ChatBubble.vue -->
<template>
  <div class="chat-bubble" :class="name">
    <h3>{{ name }}</h3>
    <p>{{ text }}</p>
  </div>
</template>

<script>
export default {
  name: 'ChatBubble',
  props: {
    name: String,
    text: String,
  },
}
</script>

<style scoped>
.chat-bubble {
  position: relative;
  background: #f0f0f0;
  border-radius: 5px;
  padding: 15px;
  margin-bottom: 20px;
}

.chat-bubble h3 {
  margin: 0 0 10px;
}

.chat-bubble p {
  margin: 0;
}

.AI1 {
  margin-left: 10px;
  background: #007bff;
  color: white;
}

.AI1::after {
  content: '';
  position: absolute;
  top: 0;
  left: -10px;
  border: 15px solid transparent;
  border-right-color: #007bff;
}

.AI2 {
  margin-right: 10px;
  background: #28a745;
  color: white;
}

.AI2::after {
  content: '';
  position: absolute;
  top: 0;
  right: -10px;
  border: 15px solid transparent;
  border-left-color: #28a745;
}
</style>
