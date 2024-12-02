<script>
export default {
  props: ['message', 'visible'],
  methods: {
    close() {
      this.$emit('onDismiss');
    }
  }
}
</script>

<template>
  <div v-if="visible" class="alert-dialog-overlay">
    <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-horiz" style="clip-path: inset(0% round 20px); width: 639px; border: 1px solid rgb(80, 80, 80); border-radius: 20px; background: rgb(20, 20, 20); padding: 44px 112px; --kobweb-arrange-spaced-by: 26px;">
      <span class="silk-span-text" style="color: white; font-size: 32px; font-weight: 700;">{{ message }}</span>
      <button class="outlined-button" @click="close">Ок!</button>
    </div>
  </div>
</template>


<style scoped>
.alert-dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.alert-dialog {
  background: white;
  padding: 20px;
  border-radius: 5px;
}
</style>
