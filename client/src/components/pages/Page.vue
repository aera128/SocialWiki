<template lang="html">
  <v-container>
    <div v-if="query && response">
      <v-card class="mb-6" rounded="lg">
        <v-img
            height="400"
            :src="images[0]"
        >
          <v-card-text align="center" justify="center">
            <v-col class="text-center" cols="12">
              <v-avatar size="250" class="mt-16 bg-light">
                <v-img alt="user" v-bind:src="profilepic">
                  <template v-slot:placeholder>
                    <v-row
                        class="fill-height ma-0 grey"
                        align="center"
                        justify="center"
                    >
                      <v-progress-circular
                          indeterminate
                          color="grey lighten-5"
                      ></v-progress-circular>
                    </v-row>
                  </template>
                </v-img>
              </v-avatar>
            </v-col>
          </v-card-text>
        </v-img>
      </v-card>
      <v-row align="center" justify="center"><h1>{{ title }}</h1></v-row>
      <v-row>
        <v-col cols="12" md="5">
          <div class="sticky-top">
            <v-sheet rounded="lg" v-if="description" class="mb-4">
              <v-card-title>
                <h2>Info</h2>
              </v-card-title>
              <v-card-text>
                <v-list dense>
                  <v-list-item v-for="(info,i) in description" :key="i">
                    <v-list-item-content>
                      <v-list-item-title>{{ i }}</v-list-item-title>
                      <v-list-item-subtitle>{{ info }}</v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-sheet>
            <v-sheet rounded="lg" min-height="268" class="mb-4" v-if="images">
              <v-card-title>
                <h2>Images</h2>
              </v-card-title>
              <v-card-text>
                <v-row v-if="maxPages > 1">
                  <v-col>
                    <div class="text-center">
                      <v-pagination
                          v-model="page"
                          :length="maxPages"
                          circle
                      ></v-pagination>
                    </div>
                  </v-col>
                </v-row>
                <v-row v-if="images !== []">
                  <v-col cols="4" v-for="(image, i) in pagedImages" :key="i">
                    <v-lazy v-if="i < 6">
                      <v-img :aspect-ratio="1" :src="image">
                        <template v-slot:placeholder>
                          <v-row
                              class="fill-height ma-0 grey"
                              align="center"
                              justify="center"
                          >
                            <v-progress-circular
                                indeterminate
                                color="grey lighten-5"
                            ></v-progress-circular>
                          </v-row>
                        </template>
                      </v-img>
                    </v-lazy>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-sheet>
          </div>
        </v-col>
        <v-col cols="12" md="7">
          <v-sheet class="mb-4" rounded="lg">
            <v-card-title>
              <h2>Publications</h2>
            </v-card-title>
          </v-sheet>
          <v-list class="rounded-lg mb-4" v-for="(post,i) in posts" :key="i">
            <v-lazy>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>
                    <v-container fluid>
                      <v-row>
                        <v-col align-self="center">
                          <v-avatar size="50" class="mr-4">
                            <v-img alt="user"
                                   :src="profilepic">
                              <template v-slot:placeholder>
                                <v-row
                                    class="fill-height ma-0 grey"
                                    align="center"
                                    justify="center"
                                >
                                  <v-progress-circular
                                      indeterminate
                                      color="grey lighten-5"
                                  ></v-progress-circular>
                                </v-row>
                              </template>
                            </v-img>
                          </v-avatar>
                          {{ title }}
                        </v-col>
                        <v-col align-self="center" class="text-right">
                          <v-list-item-action-text class="ml-auto">
                            <span class="">{{ new Date(post[0]).toLocaleDateString() }}</span>
                          </v-list-item-action-text>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-list-item-title>
                  {{ post[2] }}
                  <v-list-item-subtitle class="d-flex justify-space-around w-100 mt-5">
                    <v-badge :content="nFormatter(Math.floor(Math.random() * Math.floor(1000000)).toString())"
                             inline>
                      <v-icon color="primary">mdi-thumb-up</v-icon>
                    </v-badge>
                    <v-badge :content="nFormatter(Math.floor(Math.random() * Math.floor(100000)).toString())"
                             inline>
                      <v-icon color="primary">mdi-comment</v-icon>
                    </v-badge>
                    <v-badge :content="nFormatter(Math.floor(Math.random() * Math.floor(1000)).toString())"
                             inline>
                      <v-icon color="primary">mdi-share</v-icon>
                    </v-badge>
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-lazy>
          </v-list>
        </v-col>
      </v-row>
    </div>
    <v-overlay :value="overlay" opacity="0.9" color="#000">
      <v-progress-circular
          indeterminate
          size="150"
      >Generating
      </v-progress-circular>
    </v-overlay>
    <div v-if="notFound">
      <v-row align="center" justify="center">
        <h1 class="my-16">Not Found or Too Ambiguous</h1>
      </v-row>
    </div>
  </v-container>
</template>

<script lang="js">

import axios from "axios";
import * as qs from "qs";

export default {
  name: 'pages-facebook',
  props: [],
  mounted() {

  },
  data() {
    return {
      overlay: false,
      posts: [],
      images: [],
      pagedImages: [],
      description: [],
      title: '',
      profilepic: null,
      query: this.$route.query.q,
      page: 1,
      maxPages: 1,
      response: null,
      notFound: null
    }
  },
  methods: {
    updateData() {
      if (this.query) {
        this.overlay = true
        let params = {
          q: (!this.query || this.query === "") ? "" : this.query,
        }
        params = qs.stringify(params, {indices: false})
        axios
            .get('http://' + window.location.hostname + ':5000/generate?' + params)
            .then(r => {
              if (r.data.status === 200) {
                let data = r.data.data
                this.posts = data.posts
                this.description = data.description
                this.images = data.images
                this.title = data.title
                if (data.profilepic) {
                  this.profilepic = data.profilepic
                } else {
                  this.profilepic = this.images[1]
                }

                this.$store.commit('addWiki', {
                  'query': this.query,
                  'value': {
                    'posts': this.posts,
                    'description': this.description,
                    'images': this.images,
                    'title': this.title,
                    'profilepic': this.profilepic,
                  }
                })
                this.maxPages = this.images.length / 6 >= 1 ? Math.round(this.images.length / 6) : 1
                this.pagedImages = this.images.slice(0, 6)
                this.response = true
              } else {
                if (r.data.status === 404) {
                  this.notFound = true
                }
              }
              this.overlay = false
            })
      }
    },
    nFormatter(num, digits) {
      let si = [
        {value: 1, symbol: ""},
        {value: 1E3, symbol: " k"},
        {value: 1E6, symbol: " M"},
        {value: 1E9, symbol: " G"},
        {value: 1E12, symbol: " T"},
        {value: 1E15, symbol: " P"},
        {value: 1E18, symbol: " E"}
      ];
      let rx = /\.0+$|(\.[0-9]*[1-9])0+$/;
      let i;
      for (i = si.length - 1; i > 0; i--) {
        if (num >= si[i].value) {
          break;
        }
      }
      return (num / si[i].value).toFixed(digits).replace(rx, "$1") + si[i].symbol;
    }
  },
  computed: {},
  async created() {
    this.updateData()
  },
  watch: {
    page: function () {
      this.pagedImages = this.images.slice((this.page - 1) * 6, 6 + (this.page - 1) * 6)
    }
  }
}


</script>

<style scoped lang="scss">
.sticky-top {
  position: sticky;
  top: -100%;
}
</style>
