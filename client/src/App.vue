<template>
  <v-app id="inspire">
    <v-app-bar
        app
        color="white"
        elevation="1"
    >
      <v-container class="py-0 fill-height">
        <v-avatar
            class="mr-10"
            color="grey darken-1"
            size="32"
        >
          <v-img
              src="https://fakoamerica.typepad.com/.a/6a00d83451ce8669e2019b005615ae970b-pi"></v-img>
        </v-avatar>

        <v-btn
            v-for="link in links"
            :key="link.name"
            :to="link.route"
            text
        >
          {{ link.name }}
        </v-btn>

        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-text-field
                  v-on="on"
                  dense
                  flat
                  hide-details
                  rounded
                  solo-inverted
                  label="Search"
                  v-model="query"
                  :items="items"
                  @keyup="updateSearch"
              ></v-text-field>
            </template>
            <v-list>
              <v-list-item-group color="primary">
                <v-list-item v-for="(item,i) in items" :key="i">
                  <v-list-item-content @click="goTo(item)">
                    <v-list-item-title>{{ item }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-menu>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <vue-page-transition name="overlay-down-full">
        <router-view/>
      </vue-page-transition>
    </v-main>
  </v-app>
</template>

<script>
import wiki from "wikijs";

export default {
  name: 'App',

  components: {},
  data: () => ({
    links: [
      {name: 'Home', route: '/'},
      {name: 'About', route: '/about'},
    ],
    items: [],
    query: '',
  }),
  methods: {
    updateSearch() {
      if (this.query !== '') {
        wiki().prefixSearch(this.query, 10)
            .then(value => {
              this.items = value.results
            });
      } else {
        this.items = []
      }
    },
    goTo(item) {
      if (this.$router.currentRoute.path !== '/') {
        this.$router.push('/page/' + item)
        this.$router.go(0)
      } else {
        this.$router.push('/page/' + item)
      }
    }
  },
  watch: {}
};
</script>

<style lang="scss">
.overlay-top,
.overlay-bottom {
  background-color: #b3b3b3 !important;
  z-index: 2;
}
</style>
