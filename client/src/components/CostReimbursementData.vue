<template functional>
  <div>
    <tr>
      <td>
        <strong>Erittelyt</strong>
      </td>
      <td>
        <table v-if="props.reimbursement.length">
          <tr v-for="exp in props.reimbursement.explanations" :key="exp.id">
            <td>
              <strong>{{ exp.amount.toFixed(2) }}€&nbsp;</strong>
            </td>
            <td>{{ exp.explanation }}</td>
          </tr>
        </table>
        <span v-else>Ei oo!</span>
      </td>
    </tr>
    <tr>
      <td>
        <strong>Kuitteja</strong>
      </td>
      <td>{{ props.reimbursement.receipts.length }} kpl</td>
    </tr>
  </div>
</template>
<style lang="scss" scoped>
td {
  padding-right: 1em;
}
</style>
