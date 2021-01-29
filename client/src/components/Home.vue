<template lang="html">
  <v-container class="home">
    <v-row>
      <v-col class="text-center">
        <h1 class="display-4 my-16">Search</h1>
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-text-field
          label="Search"
          v-model="query"
          :items="items"
          @keyup="updateSearch"
          outlined
      ></v-text-field>
    </v-row>
    <v-row v-if="items.length > 0" elevation="5">
      <v-col>
        <v-list class="rounded-lg">
          <v-list-item-group color="primary">
            <v-list-item v-for="(item,i) in items" :key="i">
              <v-list-item-content @click="goTo(item)">
                <v-list-item-title>{{ item }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="js">
import wiki from 'wikijs';

export default {
  name: 'home',
  props: [],
  mounted() {

  },
  data() {
    return {
      query: '',
      items: [],
      timeout: null
    }
  },
  methods: {
    updateSearch() {
      if (this.query !== '') {
          wiki().search(this.query)
              .then(value => {
                this.items = value.results
              });
      } else {
        this.items = []
      }
    },
    goTo(item) {
      this.$router.push('/page?q=' + item)
    }
  },
  computed: {},
}


</script>

<style scoped lang="scss">
.home {

}
</style>
