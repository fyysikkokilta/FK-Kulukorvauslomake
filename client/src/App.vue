<template>
  <b-container id="app" fluid>
    <b-row>
      <b-col col md="8" lg="6" offset-md="2" offset-lg="3">
        <b-jumbotron header="FK">
          <h1 @dblclick="egg">Kulu- ja matkakorvaus</h1>
          <router-link v-if="!user" :to="{ path: '/login' }" class="float-right">Kirjaudu</router-link>
          <div v-else class="float-right">
            <router-link :to="{ name: 'view' }">Arkistoon</router-link>
            &nbsp;&nbsp;
            <router-link :to="{ name: 'home' }">Lomakkeeseen</router-link>
          </div>
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
  methods: {
    ...mapActions(['fetchUser']),
    egg() {
      window.location.href = `https://xkcd.com/${Math.floor(
        Math.random() * 2109,
      )}`;
    },
  },
  mounted() {
    this.fetchUser();
  },
};
</script>
