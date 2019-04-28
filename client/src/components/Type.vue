<script>
export default {
  functional: true,
  render(h, ctx) {
    const type = {
      TravelReimbursement: 'car',
      CostReimbursement: 'file-invoice-dollar',
    }[ctx.props.type];
    return <fa-icon size="2x" icon={type} />;
  },
};
</script>
