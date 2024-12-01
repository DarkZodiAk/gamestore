<script setup>
defineProps({
  value: {
    type: String,
    required: true,
  },
  is_rating: {
    type: Boolean,
    required: false,
    default: false
  }
})
</script>

<template>
  <div class="kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-vert" style="clip-path: inset(0% round 51px); border: 1px solid rgb(38, 38, 38); border-radius: 51px; padding: 4px 10px; --kobweb-arrange-spaced-by: 3px;">
    <img style="width: 20px; height: 20px" alt="Logout" src="@/assets/star.png" v-if="is_rating"/>
    <span class="silk-span-text" style="font-size: 16px; font-weight: 400; color: rgb(153, 153, 153);">{{ value }}</span>
  </div>
</template>

<style scoped>

</style>
