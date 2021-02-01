<template lang="html">
  <v-container class="home" fluid>
    <v-parallax dark src="https://i.pinimg.com/originals/46/1d/25/461d254f8563f8945ce3a385f289df17.jpg" style="height: calc(100vh - 90px)">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <h1 class="display-3 font-weight-thin mb-4" style="color: black">
            SocialWiki
          </h1>
          <div class="subheading">
            <v-container>
              <v-row>
                <v-col cols="12" md="6" class="mx-auto">
                  <v-text-field
                      label="Search"
                      v-model="query"
                      :items="items"
                      @keyup="updateSearch"
                      solo
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </div>
        </v-col>
      </v-row>
    </v-parallax>
    <v-row v-if="items.length > 0">
      <v-col cols="12" md="8" class="mx-auto">
        <v-card elevation="5" style="margin-top: -250px !important;">
          <v-card-text>
            <v-list>
              <v-list-item-group color="primary">
                <v-list-item v-for="(item,i) in items" :key="i">
                  <v-list-item-content @click="goTo(item)">
                    <v-list-item-title>{{ item }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card-text>
        </v-card>
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
        wiki().prefixSearch(this.query, 10)
            .then(value => {
              this.items = value.results
            });
      } else {
        this.items = []
      }
    },
    goTo(item) {
      this.$router.push('/page/' + item)
    }
  },
  computed: {},
}


</script>

<style scoped lang="scss">
.home {

}
</style>
