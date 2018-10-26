import QtQuick 2.9
import QtQuick.Window 2.2
import QtGraphicalEffects 1.0
import Qt.labs.platform 1.0

import './Component'

Window {
    id: main
    visible: false
    width: 320
    height: 240
    title: qsTr('LHAHK')

    property int tiny_font_size: 10
    property int small_font_size: 13
    property int font_size: 15
    property string font_family: 'LiHu Mono Regular'

    OutputRect {
        id: resultRect
        width: parent.width
        height: parent.height
        LinearGradient {
            width: parent.width;
            height: parent.height;
            gradient: Gradient {
                GradientStop{ position: 0.0; color: '#00D0D8EF';}
                GradientStop{ position: 0.5; color: '#300A0AEA';}
                GradientStop{ position: 1.0; color: '#00D0D8EF';}
            }
            start: Qt.point(0, 0);
            end: Qt.point(0, 300);
        }
    }

    SystemTrayIcon {
        id: systemTray
        visible: true
        iconSource: '../main.ico'
        tooltip: 'LHAHK'

        menu: Menu {
            MenuItem {
                text: qsTr('Quit')
                onTriggered: Qt.quit()
            }
        }

        onActivated: function (event) {
            if (event === SystemTrayIcon.MiddleClick) {
                if (main.visible === false) {
                    main.show()
                }
                else {
                    main.hide()
                }
            }
            else if (event === SystemTrayIcon.Context) {
                menu.open()
            }
            else if (event === SystemTrayIcon.Trigger) {
                showMessage('Mode', externer.get_mode())
            }
        }
    }

    ListModel {
        id: resultList
    }
    function output_get () {
        resultList.clear()
        resultList.append(externer.get_key_list())
    }

    function tray_info (title, content) {
        systemTray.showMessage(title, content)
    }
}
