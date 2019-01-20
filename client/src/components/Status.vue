<script>
export default {
  functional: true,
  render(h, ctx) {
    const status = {
      1: 'money-bill-wave-alt',
      2: 'thumbs-up',
      3: 'thumbs-down',
      4: 'hourglass-half',
    }[ctx.props.status];
    return <fa-icon size="2x" icon={status} />;
  },
};
</script>
