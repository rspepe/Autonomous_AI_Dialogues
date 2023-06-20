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

.chat-bubble p {
  margin: auto 10px;
  padding: 10px;
  border-radius: 10px;
  flex: 1;
}

.AI1 {
  flex-direction: row;
}

.AI1 p {
  background: white;
}

.AI2 {
  flex-direction: row-reverse;
}
.AI2 p {
  background: #94df83;
}
</style>
