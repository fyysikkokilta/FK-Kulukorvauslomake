<template>
  <b-row>
    <b-col col cols="8">
      <b-row>
        <b-input class="col-7" placeholder="Lähettäjä" v-model="params.name"/>
        <b-form-select class="col-5" v-model="params.hidden" :options="hiddenOpts"/>
      </b-row>
      <b-row>
        <b-input @input="setStart" class="col-6" placeholder="pp.kk.vvvv"/>
        <b-input @input="setEnd" class="col-6" placeholder="pp.kk.vvvv"/>
      </b-row>
      <b-row>
        <b-form-select class="col-6" v-model="params.reimbursement_type" :options="types"/>
        <b-form-select class="col-6" v-model="params.status" :options="filters"/>
      </b-row>
    </b-col>
    <b-col id="controls" col cols="4" lg="2" offset-lg="2">
      <b-row>
        <b-button class="full" variant="success" @click="search">Hae!</b-button>
      </b-row>
      <b-row>
        <a class="btn btn-primary full" :href="downloadURL">Lataa PDF:t!</a>
      </b-row>
      <b-row>
        <b-button @click="prev" class="col-4">&lt;</b-button>
        <b-badge class="col-4">
          <span>{{ Math.min(params.page+1, pages) }} / {{ pages }}</span>
        </b-badge>
        <b-button @click="next" class="col-4">&gt;</b-button>
      </b-row>
    </b-col>
  </b-row>
</template>
<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  data() {
    return {
      params: {
        page: 0,
        count: 10,
        applied_after: '',
        applied_before: '',
        name: '',
        reimbursement_type: 'all',
        status: 0,
        hidden: false,
      },
      types: [
        { value: 'all', text: 'Kaikki' },
        { value: 'travel', text: 'Matkakorvaukset' },
        { value: 'cost', text: 'Kulukorvaukset' },
      ],
      hiddenOpts: [
        { value: false, text: 'Piilottamattomat' },
        { value: true, text: 'Piilotetut' },
      ],
      filters: [
        { value: 0, text: 'Kaikki' },
        { value: 1, text: 'Käsittelemättömät' },
        { value: 2, text: 'Hyväksytyt' },
        { value: 3, text: 'Hylätyt' },
        { value: 4, text: 'Maksetut' },
      ],
    };
  },
  mounted() {
    this.search();
  },
  computed: {
    ...mapGetters(['pages']),
    downloadURL() {
      return `/api/reimbursements/pdfs?${new URLSearchParams(
        this.params,
      ).toString()}`;
    },
  },
  methods: {
    ...mapActions(['fetchReimbursements']),
    search() {
      this.fetchReimbursements({ ...this.params });
    },
    setStart(value) {
      this.params.applied_after = '';
      try {
        const [day, month, year] = value.split('.');
        this.params.applied_after = new Date(year, month - 1, day, 3)
          .toISOString()
          .split('T')[0];
      } catch (e) {
        console.log('Invalid date format', value);
      }
    },
    setEnd(value) {
      this.params.applied_before = '';
      try {
        const [day, month, year] = value.split('.');
        this.params.applied_before = new Date(year, month - 1, day, 3)
          .toISOString()
          .split('T')[0];
      } catch (e) {
        console.log('Invalid date format', value);
      }
    },
    next(ev) {
      ev.preventDefault();
      this.params.page = Math.min(this.pages - 1, this.params.page + 1);
    },
    prev(ev) {
      ev.preventDefault();
      this.params.page = Math.min(this.pages - 1, this.params.page);
      this.params.page = Math.max(0, this.params.page - 1);
    },
  },
};
</script>
<style scoped>
.badge {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.badge > span {
  font-size: 1.3em;
}
.full {
  width: 100%;
  margin-bottom: 3px;
}
</style>
