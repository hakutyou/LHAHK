import QtQuick 2.9

Rectangle {
    Component {
        id: resultComponent
        Item {
            property var result_model: model
            width: parent.width
            height: 30
            Rectangle {
                color: '#00000000'
                width: parent.width
                height: parent.height
                Text {
                    x: 10
                    width: parent.width - 20
                    height: parent.height
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                    text: role_name
                    font.family: main.font_family
                    font.pixelSize: main.small_font_size
                    clip: true
                }
                Text {
                    x: 10
                    anchors.left: parent.left
                    width: parent.width - 10
                    height: parent.height
                    horizontalAlignment: Text.AlignRight
                    verticalAlignment: Text.AlignVCenter
                    text: role_id
                    font.family: main.font_family
                    font.pixelSize: main.tiny_font_size
                    font.italic: true
                    color: "grey"
                    clip: true
                }
            }
        }
    }
    ListView {
        id: resultView
        anchors.fill: parent
        model: resultList
        delegate: resultComponent
        focus: true
    }
    ListModel {
            id: resultList
    }
    function output_get() {
        resultList.clear()
        resultList.append(con.get_key_list())
    }
}
