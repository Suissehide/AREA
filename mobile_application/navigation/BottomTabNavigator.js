import React, { useState } from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import TabBarIcon from '../components/TabBarIcon';
import HomeScreen from '../screens/HomeScreen';
import CardTest from '../screens/CardTest';

const BottomTab = createBottomTabNavigator();
const INITIAL_ROUTE_NAME = 'Login';

export default function BottomTabNavigator({ navigation, route }) {
    // Set the header title on the parent stack navigator depending on the
    // currently active tab. Learn more in the documentation:
    // https://reactnavigation.org/docs/en/screen-options-resolution.html
    navigation.setOptions({ headerTitle: getHeaderTitle(route) });
    const [test, setTest] = useState('a');
    return (
        <BottomTab.Navigator initialRouteName={INITIAL_ROUTE_NAME}>
            <BottomTab.Screen
                name="Home"
                component={CardTest}
                options={{
                    title: 'Home',
                    tabBarIcon: ({ focused }) => <TabBarIcon focused={focused} name="md-paper" />,
                }}
            />
            <BottomTab.Screen
                name="ManageWidgets"
                component={HomeScreen}
                options={{
                    title: 'Manage Widgets',
                    tabBarIcon: ({ focused }) => <TabBarIcon focused={focused} name="md-build" />,
                }}
            />
            <BottomTab.Screen
                name="Settings"
                component={HomeScreen}
                options={{
                    title: 'Account Settings',
                    tabBarIcon: ({ focused }) => <TabBarIcon focused={focused} name="md-settings" />,
                }}
            />
        </BottomTab.Navigator>
    );
}

function getHeaderTitle(route) {
    const routeName = route.state?.routes[route.state.index]?.name ?? INITIAL_ROUTE_NAME;

    switch (routeName) {
        case 'Home':
            return 'All your widgets in one place';
        case 'ManageWidgets':
            return 'Suscribe to new services and widgets';
        case 'Settings':
            return 'Account Settings';
    }
}
