<script setup>
import {RouterLink, useRouter} from "vue-router";
import {useAuthStore} from "@/stores/AuthStore.js";
import VLoader from "@/components/VLoader.vue";
import Footer from "@/components/Footer.vue";
import HeaderLite from "@/components/HeaderLite.vue";

const authStore = useAuthStore();
const router = useRouter()

const login = async () => {
    await authStore.login()

    if (!authStore.authError) {
        await router.push('/')
        console.log('no error')
    }else {
        console.log('error')
        authStore.logout()
    }
}
</script>

<template>
  <div id="root" style="width: 100%; height: 100%;" class="silk-colors_dark">
    <div class="silk-surface silk-smooth-color kobweb-box kobweb-align-top-start" style="min-height: 100vh;">
      <div class="kobweb-col kobweb-arrange-space-between kobweb-align-start" style="width: 100%; height: 100%;">
        <div class="kobweb-col kobweb-arrange-top kobweb-align-center-horiz" style="width: 100%; height: 100%;">
          <HeaderLite/>
          <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-horiz" style="width: 448px; --kobweb-arrange-spaced-by: 25px;">
            <span class="silk-span-text" style="font-size: 34px;">Вход</span>

            <form @keydown.enter.prevent="login" @submit.prevent="login">
              <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-center-horiz"
                   style="clip-path: inset(0% round 10px); background: rgb(15, 15, 15); border: 1px solid rgb(38, 38, 38); border-radius: 10px; width: 448px; padding: 40px; --kobweb-arrange-spaced-by: 25px;">
                <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start" style="width: 100%; --kobweb-arrange-spaced-by: 12px;">
                  <span class="silk-span-text">Введите логин</span>
                  <input type="text" placeholder="Введите логин" v-model="authStore.username">

                </div>
                <div class="kobweb-col kobweb-arrange-spaced-by kobweb-arrange-start kobweb-align-start" style="width: 100%; --kobweb-arrange-spaced-by: 12px;">
                  <span class="silk-span-text">Пароль</span>
                  <input type="text" placeholder="Введите пароль" v-model="authStore.password">

                </div>
                <button class="primary-button" type="submit" v-if="!authStore.loading">
                  <span class="silk-span-text" style="font-size: 14px; line-height: 1.5;">Войти</span>
                </button>
                <VLoader class="auth-loader" v-else></VLoader>
                <div class="kobweb-row kobweb-arrange-start kobweb-align-top kobweb-arrange-spaced-by" style="--kobweb-arrange-spaced-by: 12px;">
                  <span>Нет аккаунта?</span> <RouterLink to="/register">Зарегистрироваться</RouterLink>
                </div>
              </div>
            </form>

          </div>
        </div>
       <Footer/>
      </div>
    </div>
  </div>
</template>

<style scoped>

input {
    margin-bottom: 18px;
    border-radius: 6px;
    border: 1px solid rgb(38, 38, 38);
    background: rgb(20, 20, 20);
    color: #FFFFFF;
    width: 100%;
    padding: 16px;
    font-size: 16px;
    outline: 0;
}

</style>
