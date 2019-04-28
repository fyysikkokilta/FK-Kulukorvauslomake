<template>
  <b-modal
    ref="modal"
    v-if="reimbursement"
    :visible="visible"
    @hidden="closed"
    centered
    :title="`${type} ${date}`"
  >
    <table>
      <ReimbursementCommon :reimbursement="reimbursement"/>
      <hr>
      <CostReimbursementData :reimbursement="reimbursement" v-if="isCost"/>
      <TravelReimbursementData :reimbursement="reimbursement" v-else/>
    </table>

    <div v-if="!hasProcessed">
      <label for="pr" id="label">Käsitelty raadin kokouksessa:</label>
      <b-input id="pr" v-model="meeting"/>
    </div>
    <div v-else>
      <b-alert id="alert" show>Käsitelty raadin kokouksessa: {{ reimbursement.processed }}</b-alert>
    </div>

    <template slot="modal-footer">
      <template>
        <b-button
          variant="success"
          @click="accept"
          v-if="reimbursement.status === STATUS.PENDING"
          :disabled="!meeting.length"
        >Hyväksy</b-button>
        <b-button
          variant="danger"
          @click="reject"
          v-if="reimbursement.status === STATUS.PENDING"
          :disabled="!meeting.length"
        >Hylkää</b-button>

        <b-button
          variant="success"
          @click="markPaid"
          v-if="reimbursement.status === STATUS.OK"
        >Merkitse maksetuksi</b-button>
      </template>

      <template>
        <b-button variant="warning" @click="hide" v-if="reimbursement.hidden">Piilota</b-button>
        <b-button
          variant="warning"
          @click="unhide"
          v-if="!reimbursement.hidden && reimbursement.status !== STATUS.PENDING"
        >Piilota</b-button>
      </template>
      <b-button variant="primary" @click="close">Sulje</b-button>
    </template>
  </b-modal>
</template>
<script>
import { mapActions } from 'vuex';

import ReimbursementCommon from '@/components/ReimbursementCommon.vue';
import CostReimbursementData from '@/components/CostReimbursementData.vue';
import TravelReimbursementData from '@/components/TravelReimbursementData.vue';

const STATUS = {
  PENDING: 1,
  OK: 2,
  NOK: 3,
  PAID: 4,
};

export default {
  components: {
    CostReimbursementData,
    TravelReimbursementData,
    ReimbursementCommon,
  },
  props: ['reimbursement'],
  data() {
    return {
      visible: false,
      meeting: '',
      STATUS,
    };
  },
  computed: {
    hasProcessed() {
      return !!this.reimbursement.processed.length;
    },
    type() {
      return this.isCost ? 'Kulukorvaus' : 'Matkakorvaus';
    },
    date() {
      return new Date(this.reimbursement.applied).toLocaleDateString('fi');
    },
    isCost() {
      return this.reimbursement.classtype === 'CostReimbursement';
    },
  },
  methods: {
    ...mapActions(['updateReimbursement']),
    update() {
      this.reimbursement.processed = this.meeting;
      this.updateReimbursement(this.reimbursement);
    },
    hide() {
      this.reimbursement.hidden = true;
      this.update();
    },
    unhide() {
      this.reimbursement.hidden = false;
      this.update();
    },
    accept() {
      this.reimbursement.status = STATUS.OK;
      this.update();
    },
    reject() {
      this.reimbursement.status = STATUS.NOK;
      this.update();
    },
    markPaid() {
      this.reimbursement.status = STATUS.PAID;
      this.update();
    },
    closed() {
      this.visible = false;
      this.$emit('closed');
    },
    close() {
      this.$refs.modal.hide();
    },
  },
  watch: {
    reimbursement(next, prev) {
      // We want to set our modal visible
      // whenever new value for reimbursement
      // is received given that it is not set to
      // null.
      this.visible = !!next;
    },
  },
};
</script>
<style lang="scss" scoped>
#pr {
  display: inline-block;
  width: 30%;
}
#label {
  width: 60%;
}
#alert {
  padding: 1em;
  margin: 1em;
}
</style>
