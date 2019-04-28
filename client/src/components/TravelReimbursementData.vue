<template functional>
  <div>
    <tr>
      <td>
        <strong>Rekisteritunnus</strong>
      </td>
      <td>
        <h4>
          <b-badge variant="dark">{{ props.reimbursement.licenseNumber }}</b-badge>
        </h4>
      </td>
    </tr>
    <tr>
      <td>
        <strong>Matkustajat</strong>
      </td>
      <td>{{ props.reimbursement.passengers }}</td>
    </tr>
    <tr>
      <td>
        <strong>Reitti</strong>
      </td>
      <td>{{ props.reimbursement.route }}</td>
    </tr>
    <tr>
      <td>
        <strong>Pituus</strong>
      </td>
      <td>{{ props.reimbursement.distance.toFixed(0) }} km</td>
    </tr>
  </div>
</template>
<style lang="scss" scoped>
td {
  padding-right: 1em;
}
</style>
