<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" disable-resize-watcher app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            SocialWiki
          </v-list-item-title>
          <v-list-item-subtitle>
            wikipedia converter
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list nav>
        <router-link to="/" class="text-decoration-none">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
        <router-link to="/about" class="text-decoration-none">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-information</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>About</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app dense>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <vue-page-transition name="overlay-left-full">
        <router-view></router-view>
      </vue-page-transition>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  components: {},
  data: () => ({drawer: false}),
  methods: {},
  watch: {
    $route() {
      setTimeout(() => {
        this.drawer = false
      },300)
    }
  }
};
</script>

<style lang="scss">
.overlay-left,
.overlay-right {
  background-color: #a7a7a7 !important;
  z-index: 9998;
}
</style>
