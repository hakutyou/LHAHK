import QtQuick 2.9
import QtQuick.Window 2.2
import QtGraphicalEffects 1.0

import './Component'

Window {
    id: main
    visible: true
    width: 320
    height: 240
    title: qsTr("LHAHK")

    property int tiny_font_size: 10
    property int small_font_size: 13
    property int font_size: 15
    property string font_family: 'LiHu Mono Regular'

    OutputRect {
        id: resultRect
        objectName: 'resultRect'
        width: parent.width
        height: parent.height
        LinearGradient {
            width: parent.width;
            height: parent.height;
            gradient: Gradient {
                GradientStop{ position: 0.0; color: "#00D0D8EF";}
                GradientStop{ position: 0.5; color: "#300A0AEA";}
                GradientStop{ position: 1.0; color: "#00D0D8EF";}
            }
            start: Qt.point(0, 0);
            end: Qt.point(0, 300);
        }
    }
}
