<template lang="html">
  <v-container>
    <div v-if="query && response">
      <v-card class="mb-6" rounded="lg">
        <v-img height="400" :src="images[1] ? images[1] : images[0]">
          <v-card-text align="center" justify="center">
            <v-col class="text-center" cols="12">
              <v-avatar size="250" class="mt-16 bg-light" style="background-color: rgba(0,0,0,0.6)">
                <v-img alt="user" v-bind:src="profilepic ? profilepic: images[0]">
                  <template v-slot:placeholder>
                    <v-row class="fill-height ma-0 grey" align="center" justify="center">
                      <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                    </v-row>
                  </template>
                </v-img>
              </v-avatar>
            </v-col>
          </v-card-text>
        </v-img>
      </v-card>
      <v-row align="center" justify="center"><h1>{{ query }}</h1></v-row>
      <v-row class="align-items-start justify-space-around d-flex">
        <v-col cols="12" md="5" class="sticky-top">
          <v-sheet rounded="lg" v-if="description" class="mb-4">
            <v-card-title>
              <h2>Info</h2>
            </v-card-title>
            <v-card-text>
              <v-list dense>
                <v-list-item v-for="(info,i) in description" :key="i">
                  <v-list-item-content>
                    <v-list-item-title>{{ i }}</v-list-item-title>
                    <v-list-item-subtitle>
                      <div v-if="typeof info === 'object' && !info['date']">
                        <div v-for="(child, j) in info" :key="j">{{ child }}</div>
                      </div>
                      <div v-if="typeof info === 'object' && info['date']">
                        {{ new Date(info['date']).toLocaleString() }}
                      </div>
                      <div v-if="typeof info === 'string' && validURL(info)"><a target="_blank"
                                                                                :href="'//'+info">{{ info }}</a></div>
                      <div v-if="typeof info === 'string' && !validURL(info)">{{ info }}</div>
                      <div v-if="info instanceof Date">{{ info.toLocaleString() }}</div>
                    </v-list-item-subtitle>
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
                    <v-pagination v-model="page" :length="maxPages" circle></v-pagination>
                  </div>
                </v-col>
              </v-row>
              <v-row v-if="images !== []">
                <v-col cols="4" v-for="(image, i) in pagedImages" :key="i">
                  <v-lazy v-if="i < 6">
                    <v-img :aspect-ratio="1" :src="image">
                      <template v-slot:placeholder>
                        <v-row class="fill-height ma-0 grey" align="center" justify="center">
                          <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                        </v-row>
                      </template>
                    </v-img>
                  </v-lazy>
                </v-col>
              </v-row>
            </v-card-text>
          </v-sheet>
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
                          <v-avatar size="50" class="mr-4" style="background-color: rgba(0,0,0,0.6)">
                            <v-img alt="user" :src="profilepic ? profilepic: images[0]">
                              <template v-slot:placeholder>
                                <v-row class="fill-height ma-0 grey" align="center" justify="center">
                                  <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                                </v-row>
                              </template>
                            </v-img>
                          </v-avatar>
                          {{ query }}
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
                    <v-badge :content="nFormatter(post[3])"
                             inline>
                      <v-icon color="primary">mdi-thumb-up</v-icon>
                    </v-badge>
                    <v-badge :content="nFormatter(post[4])"
                             inline>
                      <v-icon color="primary">mdi-comment</v-icon>
                    </v-badge>
                    <v-badge :content="nFormatter(post[5])"
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
    <v-overlay :absolute="true" :value="overlay" opacity="0.9" color="#000" style="z-index: 1">
      <v-progress-circular indeterminate size="150">Generating</v-progress-circular>
    </v-overlay>
    <div v-if="notFound">
      <v-row align="center" justify="center" class="fill-height mt-16">
        <h1 class="display-4 font-weight-thin mt-16">404 - Not Found</h1>
      </v-row>
    </div>
  </v-container>
</template>

<script lang="js">

import axios from "axios";
import wiki from 'wikijs';

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
      profilepic: null,
      query: this.$route.params.id,
      text: '',
      page: 1,
      maxPages: 1,
      response: null,
      notFound: null,
    }
  },
  methods: {
    updateData() {
      if (this.query) {
        this.overlay = true
        wiki().page(this.query).then(page => {
          page.fullInfo().then(infos => {
            infos = infos.general
            let list_infos = {}
            for (const info in infos) {
              if (info !== 'signatureAlt') {
                if (typeof infos[info] === 'string') {
                  if (!infos[info].includes('.jpg') && !infos[info].includes('.png') && !infos[info].includes('.svg')) {
                    list_infos[info] = infos[info]
                  }
                } else if (typeof infos[info] === 'number') {
                  list_infos[info] = infos[info].toString()
                }
                else {
                  list_infos[info] = infos[info]
                }
              }
            }
            this.description = list_infos
          })
          page.mainImage().then(image => {
            if (image.includes('.jpg') || image.includes('.png')) this.profilepic = image
          })
          page.images().then(images => {
            this.images = images
            this.images = this.images.filter(image => image.includes('.jpg'))
            this.maxPages = this.images.length / 6 >= 1 ? Math.round(this.images.length / 6) : 1
            this.pagedImages = this.images.slice(0, 6)
          })
          page.summary().then(summary => {
            this.text = summary
            page.rawContent().then(content => {
              this.text = this.text + ' ' + content
              let url = 'http://' + window.location.hostname + ':5000/api/generate'
              url.replace(" ", "%20")
              axios
                  .post(url, {
                    'query': this.query,
                    'text': this.text
                  })
                  .then(r => {
                    if (r.data.status === 200) {
                      let data = r.data.data
                      this.posts = data.posts
                      this.response = true
                    } else {
                      if (r.data.status === 404) {
                        this.notFound = true
                      }
                    }
                    this.overlay = false
                  })
            })
          })
        }, () => {
          this.notFound = true
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
    },
    validURL(str) {
      let pattern = new RegExp('^(https?:\\/\\/)?' + // protocol
          '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
          '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
          '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
          '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
          '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator
      return !!pattern.test(str);
    }
  },
  computed: {},
  async created() {
    this.updateData()
  },
  watch: {
    page: function () {
      this.pagedImages = this.images.slice((this.page - 1) * 6, 6 + (this.page - 1) * 6)
    },
    watch: {
      'this.$router.params.id': function (id) {
        console.log(id)
      }
    }
  }
}


</script>

<style scoped lang="scss">
.sticky-top {
  position: -webkit-sticky;
  position: sticky;
  bottom: 1rem;
  align-self: flex-end;
}
</style>
