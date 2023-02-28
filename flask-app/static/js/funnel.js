function generateFunnel(id) {
  am5.ready(function() {
    $("#" + id).addClass("w-full h-[500px]")
    // Create root element
    var root = am5.Root.new(id);
    root._logo.dispose();

    // Set themes
    root.setThemes([
      am5themes_Animated.new(root)
    ]);

    // Create chart
    var chart = root.container.children.push(am5percent.SlicedChart.new(root, {
      layout: root.verticalLayout,
    }));

    // Create series
    var series = chart.series.push(am5percent.FunnelSeries.new(root, {
      alignLabels: false,
      orientation: "vertical",
      valueField: "value",
      categoryField: ""
    }));

    // Set data
    series.data.setAll([
      { value: 10 },
      { value: 9 },
      { value: 8 },
      { value: 7 },
    ]);

    // hide labels
    series.labels.template.setAll({
      fontSize: 20,
      textAlign: "center",
      fill: am5.color(0xffffff),
      text: "{category}",
      oversizedBehavior: "hide",
      maxWidth: 0
    });

    // Play initial series animation
    series.appear();

    // Make stuff animate on load
    chart.appear(1000, 100);
    $(` <div class="animate-fade-in absolute flex items-center flex-col top-0 left-0 bottom-0 right-0 py-7 px-11 text-white text-xl text-center">
      <p class="max-w-[100%] h-[25%] items-center flex">
        Subit de la pression pour passer plus de temps chez l'autre
      </p>
      <p class="max-w-[90%] h-[25%] items-center flex">
        Est informé du contexte juridique ou autre sujet associé au conflit
      </p>
      <p class="max-w-[80%] h-[25%] items-center flex">
        Déforme les souvenirs
      </p>
      <p class="max-w-[70%] h-[25%] items-center flex">
        Change d'attitude lorsqu'il est en présence des deux parents
      </p>
    </div>`).insertAfter("#" + id)
  }); // end am5.ready()
}