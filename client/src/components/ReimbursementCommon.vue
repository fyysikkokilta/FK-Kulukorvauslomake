<template functional>
  <div>
    <tr>
      <td>
        <strong>Lähettäjä</strong>
      </td>
      <td>{{ props.reimbursement.name }}</td>
    </tr>
    <tr>
      <td>
        <strong>Summa</strong>
      </td>
      <td>{{ props.reimbursement.amount.toFixed(2) }}€</td>
    </tr>
    <tr>
      <td>
        <strong>Kuvaus</strong>
      </td>
      <td>{{ props.reimbursement.description }}</td>
    </tr>
  </div>
</template>
<style lang="scss" scoped>
td {
  padding-right: 1em;
}
</style>
