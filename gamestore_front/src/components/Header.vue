<script setup>

import {useGameStore} from "@/stores/GameStore.js";
import {onMounted} from "vue";
const gameStore = useGameStore();

onMounted(async () => {
    await gameStore.updateCountInCart()
})

</script>

<template>
  <div class="kobweb-align-center-horiz align-center-hor" style="width: 100%; padding: 30px 0px;">
    <div class="width-lim kobweb-row kobweb-arrange-space-between kobweb-align-center-vert">
      <RouterLink to="/">
        <span class="silk-span-text" style="font-size: 22px; font-weight: 800;">GameStore</span>
      </RouterLink>
      <div class="kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-vert" style="clip-path: inset(0% round 12px); background: rgb(15, 15, 15); border: 1px solid rgb(38, 38, 38); border-radius: 12px; width: 678px; padding: 0px 0px 0px 16px; --kobweb-arrange-spaced-by: 12px;">
        <img class="icon" style="color: rgb(84, 84, 84); margin: 10px 0 10px 0" alt="Search" src="@/assets/search.png"/>
        <input class="silk-input silk-input-size_xs" type="text" placeholder="Поиск игры..." spellcheck="false">
      </div>
      <div class="kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-vert" style="--kobweb-arrange-spaced-by: 30px;">
        <div class="kobweb-row kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-vert" style="--kobweb-arrange-spaced-by: 4px;">
          <span class="silk-span-text">{{gameStore.cartCount.count}}</span>
          <RouterLink to="/cart">
            <img class="icon" alt="Basket" src="@/assets/cart.png"/>
          </RouterLink>
        </div>
        <RouterLink to="/wishlist">
          <img class="icon" alt="Wishlist" src="@/assets/list.png"/>
        </RouterLink>
        <img class="icon" alt="Logout" src="@/assets/logout.png" @click="logout"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
input {
  --silk-input-placeholder-color: rgb(84, 84, 84);
  --silk-input-placeholder-opacity: 1;
  width: 100%;
  font-size: 16px;
  padding: 20px 0 20px 0;
}
</style>
