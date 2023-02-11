import QtQuick 2.2
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.2

ApplicationWindow {
    width: 720
    height: 480
    visible: true

    Rectangle {
        anchors.fill: parent
        color: "black"
        Label {
            anchors.centerIn: parent
            text: updater.version
            font.pixelSize: 60
        }
    }
    Item {
        height: 80
        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
        }
        RowLayout {
            anchors.fill: parent
            anchors.rightMargin: 40
            Item {
                Layout.fillWidth: true
            }
            Label {
                id: updateLabel
                height: 80
                font.pixelSize: 22
                states: [
                    State {
                        when: updater.has_update
                        PropertyChanges {
                            target: updateLabel
                            text: "Has updates"
                            color: "red"
                        }
                    },
                    State {
                        when: !updater.has_update
                        PropertyChanges {
                            target: updateLabel
                            text: "Has not updates"
                            color: "blue"
                        }
                    }
                ]
            }
            Button {
                text: "Update"
                enabled: updater.has_update
                onPressed: {
                    updater.updating()
                }
            }
        }
    }
}