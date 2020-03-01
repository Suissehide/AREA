import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import TabBarIcon from '../components/TabBarIcon';
import ServiceScreen from '../screens/ServiceScreen';
import WidgetScreen from '../screens/WidgetScreen';
import AccountScreen from '../screens/AccountScreen';

const BottomTab = createBottomTabNavigator();
const INITIAL_ROUTE_NAME = 'Login';

export default function BottomTabNavigator({ navigation, route }) {
    navigation.setOptions({ headerTitle: getHeaderTitle(route) });

    return (
        <BottomTab.Navigator initialRouteName={INITIAL_ROUTE_NAME}>
            <BottomTab.Screen
                name="Home"
                component={WidgetScreen}
                options={{
                    title: 'Home',
                    tabBarIcon: ({ focused }) => <TabBarIcon focused={focused} name="md-paper" />,
                }}
            />
            <BottomTab.Screen
                name="ManageWidgets"
                component={ServiceScreen}
                options={{
                    title: 'Manage Widgets',
                    tabBarIcon: ({ focused }) => <TabBarIcon focused={focused} name="md-build" />,
                }}
            />
            <BottomTab.Screen
                name="Settings"
                component={AccountScreen}
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
