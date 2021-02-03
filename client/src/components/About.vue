<template lang="html">

  <v-container class="about">
    <v-row>
      <v-col>
        <h1 class="font-weight-thin">About</h1>
      </v-col>
    </v-row>
    <hr class="my-4">
    <v-row class="mt-4">
      <v-col cols="12" sm="6">
        <v-card>
          <v-card-title class="font-weight-thin">
            Matthieu MERCIER
          </v-card-title>
          <v-card-subtitle>
            Student - Master 2 Informatique Université de Caen
          </v-card-subtitle>
          <v-card-text>
            <v-btn color="primary" href="https://github.com/aera128" target="_blank">
              <v-icon left> mdi-github</v-icon>
              GitHub
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6">
        <v-card>
          <v-card-title class="font-weight-thin">
            Alexandre LELOUTRE
          </v-card-title>
          <v-card-subtitle>
            Student - Master 2 Informatique Université de Caen
          </v-card-subtitle>
          <v-card-text>
            <v-btn color="primary" href="https://github.com/ALeloutre" target="_blank">
              <v-icon left> mdi-github</v-icon>
              GitHub
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2 class="font-weight-thin">Frontend</h2>
        <hr class="my-4">
        <v-list>
          <v-list-item v-for="(techno,i) in technos_front" :key="i">
            <v-list-item-title><a :href="techno.href" target="_blank" class="text-decoration-none">{{ techno.name }}</a></v-list-item-title>
          </v-list-item>
        </v-list>
        <h2 class="font-weight-thin mt-4">Backend</h2>
        <hr class="my-4">
        <v-list>
          <v-list-item v-for="(techno,i) in technos_back" :key="i">
            <v-list-item-title><a :href="techno.href" target="_blank" class="text-decoration-none">{{ techno.name }}</a></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>

</template>

<script lang="js">

export default {
  name: 'about',
  props: [],
  mounted() {

  },
  data() {
    return {
      technos_front: [
        {name: 'Vue CLI', href: "https://vuejs.org/"},
        {name: 'Vue.js', href: "https://vuejs.org/"},
        {name: 'Vue Router', href: "https://router.vuejs.org/"},
        {name: 'Vuetify', href: "https://vuetifyjs.com/en/"},
        {name: 'wikijs', href: "https://github.com/dijs/wiki"},
        {name: 'axios', href: "https://github.com/axios/axios"},
        {name: 'vue-page-transition', href: "https://github.com/Orlandster/vue-page-transition"},
      ],
      technos_back: [
        {name: 'Python', href: "https://www.python.org/"},
        {name: 'Flask', href: "https://flask.palletsprojects.com/en/1.1.x/"},
        {name: 'Flask CORS', href: "https://flask-cors.readthedocs.io/en/latest/"},
        {name: 'Flask Restful', href: "https://flask-restful.readthedocs.io/en/latest/"},
        {name: 'SpaCy', href: "https://spacy.io/"},
        {name: 'DateRangeParser ', href: "https://pypi.org/project/DateRangeParser/"},
        {name: 'SqliteDict', href: "https://pypi.org/project/sqlitedict/"},
      ],
    }
  },
  methods: {},
  computed: {}
}


</script>

<style scoped lang="scss">
.about {

}
</style>
