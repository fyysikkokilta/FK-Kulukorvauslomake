<template>
  <div>
    <ReimbursementModal
      :reimbursement="reimbursement"
      @closed="modalClosed"
    />
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Haettu</th>
          <th scope="col">Lähettäjä</th>
          <th scope="col">Tyyppi</th>
          <th scope="col">Tila</th>
          <th scope="col"/>
        </tr>
      </thead>
      <tbody>
        <tr :id="`r-${r.id}`" :key="r.id" v-for="r in reimbursements.data">
          <b-popover
            placement="top"
            triggers="hover"
            :title="`Summa ${r.amount.toFixed(2)}€`"
            :content="r.description"
            :target="`r-${r.id}`"
          />
          <td scope="row">{{ new Date(r.applied).toLocaleDateString('fi') }}</td>
          <td>{{ r.name }}</td>
          <td>
            <Type class="icon-container" :type="r.classtype"/>
          </td>
          <td>
            <Status class="icon-container" :status="r.status"/>
          </td>
          <td class="buttons">
            <a class="btn btn-primary" :href="`/api/reimbursements/${r.id}/pdf`">
              <fa-icon icon="file-pdf" size="lg"/>
            </a>
            <b-button @click="show(r)">
              <fa-icon icon="search-plus" size="lg"/>
            </b-button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import { mapState, mapActions } from 'vuex';
import ReimbursementModal from '@/components/ReimbursementModal.vue';
import Type from '@/components/Type.vue';
import Status from '@/components/Status.vue';
export default {
  components: { Type, Status, ReimbursementModal },
  data() {
    return {
      reimbursement: null,
    };
  },
  computed: mapState(['reimbursements']),
  methods: {
    show(reimbursement) {
      this.reimbursement = reimbursement;
    },
    modalClosed() {
      this.reimbursement = null;
    }
  },
};
</script>
<style scoped>
.icon-container {
  display: flex;
  flex-direction: column;
}
.buttons {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}
</style>
