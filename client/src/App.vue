<template>
  <b-container id="app" fluid>
    <b-row>
      <b-col col md="8" lg="6" offset-md="2" offset-lg="3">
        <b-jumbotron header="FK">
          <h1>Kulu- ja matkakorvaus</h1>
          <router-link v-if="!user" :to="{ path: '/login' }" class="float-right">Kirjaudu</router-link>
          <router-link v-else :to="{ name: 'view' }" class="float-right">Arkistoon</router-link>
        </b-jumbotron>
      </b-col>
    </b-row>
    <b-row>
      <b-col col md="8" lg="6" offset-md="2" offset-lg="3">
        <router-view/>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
import { mapActions, mapState } from 'vuex';
export default {
  computed: mapState(['user']),
  methods: mapActions(['fetchUser']),
  mounted() {
    this.fetchUser();
  },
};
</script>
