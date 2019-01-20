<template>
  <div>
    <b-modal
      title="cost"
      v-if="reimbursement && reimbursement.classtype === 'CostReimbursement'"
      :visible="visible"
      @hidden="closed"
    />
    <b-modal
      title="travel"
      v-if="reimbursement && reimbursement.classtype === 'TravelReimbursement'"
      :visible="visible"
      @hidden="closed"
    />
  </div>
</template>
<script>
export default {
  props: ['reimbursement'],
  data() {
    return { visible: false };
  },
  methods: {
    closed() {
      this.visible = false;
      this.$emit('closed');
    }
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
