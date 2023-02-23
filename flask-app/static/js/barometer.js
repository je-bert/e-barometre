const percentToDegree = p => p * 360;
const degreeToRadian = d => d * Math.PI / 180;
const percentToRadian = p => degreeToRadian(percentToDegree(p));
class Needle {
  constructor(props) {
    this.svg = props.svg;
    this.group = this.svg.append('g');
    this.len = props.len;
    this.radius = props.radius;
    this.x = props.x;
    this.y = props.y;
  }

  render() {
    this.group.attr('transform', `translate(${this.x},${this.y})`)
    this.group
      .append('circle')
      .attr('class', 'c-chart-gauge__needle-base fill-[#555555] dark:fill-white')
      .attr('cx', 0)
      .attr('cy', 0)
      .attr('r', this.radius);

    this.group
      .append('path')
      .attr('class', 'c-chart-gauge__needle fill-[#555555] dark:fill-white')
      .attr('d', this._getPath(0));
  }

  animateTo(p) {
    this.group
      .transition()
      .delay(500)
      .ease('elastic')
      .duration(3000)
      .select('path')
      .tween('progress', () => {
        const self = this;
        const lastP = this.lastP || 0;
        return function(step) {
          const progress = lastP + step * (p - lastP);
          d3.select(this)
            .attr('d', self._getPath(progress))
        };
      })
      .each('end', () => this.lastP = p);
  }

  _getPath(p) {
    const thetaRad = percentToRadian(p / 2),
      centerX = 0,
      centerY = 0,
      topX = centerX - this.len * Math.cos(thetaRad),
      topY = centerY - this.len * Math.sin(thetaRad),
      leftX = centerX - this.radius * Math.cos(thetaRad - Math.PI / 2),
      leftY = centerY - this.radius * Math.sin(thetaRad - Math.PI / 2),
      rightX = centerX - this.radius * Math.cos(thetaRad + Math.PI / 2),
      rightY = centerY - this.radius * Math.sin(thetaRad + Math.PI / 2);
    return `M ${leftX} ${leftY} L ${topX} ${topY} L ${rightX} ${rightY}`;
  }
}

class GaugeChart {
  constructor(props) {
    this.svg = props.svg;
    this.group = this.svg.append('g');
    this.outerRadius = props.outerRadius;
    this.innerRadius = props.innerRadius;
    this.width = this.outerRadius * 2;
    this.height = this.outerRadius * 1.2;
    
    this.needle = new Needle({
      svg: this.svg,
      len: this.outerRadius * 0.65,
      radius: this.innerRadius * 0.15,
      x: this.outerRadius,
      y: this.outerRadius
    });
  }

  render() {
    const gradient = this.svg.append('defs')
      .append('linearGradient')
      .attr('id', 'c-chart-gauge__gradient');
    const arc = d3.svg.arc();
    
    this.svg
      .attr('width', this.width)
      .attr('height', this.height);

    gradient
      .append('stop')
      .attr('offset', '0%')
      .attr('style', 'stop-color: green;');
    gradient
      .append('stop')
      .attr('offset', '33%')
      .attr('style', 'stop-color: orange;');
    gradient
      .append('stop')
      .attr('offset', '66%')
      .attr('style', 'stop-color: orange;');
    gradient
      .append('stop')
      .attr('offset', '100%')
      .attr('style', 'stop-color: red;');

    arc
      .innerRadius(this.innerRadius)
      .outerRadius(this.outerRadius)
      .startAngle(-Math.PI / 2)
      .endAngle(Math.PI / 2);

    this.group
      .attr("width", this.width)
      .attr("height", this.height)
      .append("path")
      .attr("d", arc)
      .attr("fill", "url(#c-chart-gauge__gradient)")
      .attr("transform", `translate(${this.outerRadius},${this.outerRadius})`);
      
    this.needle.render();
  }
  
  animateTo(p) {
    this.needle.animateTo(p);
  }
}

function generateGauge(id, value, title) {
  const svg = d3.select('#' + id).append('svg')
      .attr('class', 'c-chart-gauge');
  const gaugeChart = new GaugeChart({
    svg: svg,
    outerRadius: 80,
    innerRadius: 60
  });

  
  gaugeChart.render();
  $(`<h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">${title}</h2>`).insertBefore("#" + id)
  gaugeChart.animateTo(value);
}
