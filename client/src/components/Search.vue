<template>
  <b-row>
    <b-col col cols="8">
      <b-row>
        <b-input @input="search" placeholder="Lähettäjä" v-model="params.name"/>
      </b-row>
      <b-row>
        <b-input @input="setStart" class="col-6" placeholder="pp.kk.vvvv"/>
        <b-input @input="setEnd" class="col-6" placeholder="pp.kk.vvvv"/>
      </b-row>
      <b-row>
        <b-form-select
          @input="search"
          class="col-6"
          v-model="params.reimbursement_type"
          :options="types"
        />
        <b-form-select @change="search" class="col-6" v-model="params.status" :options="filters"/>
      </b-row>
    </b-col>
    <b-col id="controls" col cols="4" lg="2" offset-lg="2">
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
      },
      types: [
        { value: 'all', text: 'Kaikki' },
        { value: 'travel', text: 'Matkakorvaukset' },
        { value: 'cost', text: 'Kulukorvaukset' },
      ],
      filters: [
        { value: 0, text: 'Kaikki' },
        { value: 4, text: 'Käsittelemättömät' },
        { value: 2, text: 'Hyväksytyt' },
        { value: 3, text: 'Hylätyt' },
      ],
    };
  },
  mounted() {
    this.search();
  },
  computed: mapGetters(['pages']),
  methods: {
    ...mapActions(['fetchReimbursements']),
    search() {
      this.fetchReimbursements({ ...this.params });
    },
    setStart(value) {},
    setEnd(value) {},
    next(ev) {
      ev.preventDefault();
      this.params.page = Math.min(this.pages - 1, this.params.page + 1);
      this.search();
    },
    prev(ev) {
      ev.preventDefault();
      this.params.page = Math.min(this.pages - 1, this.params.page);
      this.params.page = Math.max(0, this.params.page - 1);
      this.search();
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
#controls {
  display: flex;
  flex-direction: column-reverse;
}
</style>
